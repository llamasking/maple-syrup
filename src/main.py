import time
from utils.config import config
from discord import ApplicationContext, Bot, Embed, InteractionResponse, option
from generators.TextGenerator import TextGenerator
from generators.ConversationalGenerator import ConversationalGenerator

# Warm up generator
gpt_generator = TextGenerator()
conversational_generator = ConversationalGenerator()
bot = Bot(debug_guilds=config["DISCORD_DEBUG_GUILDS"])


@bot.event
async def on_ready():
    print(f"Bot ready! Logged in as '{bot.user.name}' ({bot.user.id}).")


@bot.slash_command(name="gpt", description="Generates text starting with the provided prompt.")
@option("prompt", str, description="Text prompt to start the generation with.")
@option("num_results", int,
        description="Number of results to generate.",
        default=1,
        min_value=1,
        max_value=config["TEXT_GENERATION_MAXIMUM_RESULTS"]
        )
async def command_generate_gpt(
    ctx: ApplicationContext,
    prompt: str,
    num_results: int = 1
):
    """
    Generates text starting with the provided prompt.

    Parameters:
        prompt (str): Prompt used to generate text from.
        num_results (int): The number of results to generate. (Clamped by config).
    """
    # Send defer response (change to "Thinking...")
    await ctx.defer()

    # Check permitted number of results requested
    num_results: int = min(num_results, config["TEXT_GENERATION_MAXIMUM_RESULTS"])

    # Generate results
    start_time = time.time()
    results = gpt_generator(prompt, num_results=num_results)
    end_time = time.time()

    # Design embed
    embed = Embed(title="Text Generation Results", color=3743206)
    embed.set_footer(
        text=f"AI Model: {config['TEXT_GENERATION_MODEL']} -- Generation took {end_time-start_time:.2f}s")
    embed.add_field(name="Prompt", value=prompt, inline=False)
    for index, result in enumerate(results):
        embed.add_field(name=f"Result {index + 1}", value=result, inline=False)
    await ctx.respond(embed=embed)


@bot.slash_command(name="converse", description="Generates a response to the provided message.")
@option("message", str, description="Text prompt to start the generation with.")
async def command_converse(ctx: ApplicationContext, message: str):
    """
    Generates a conversational response from the given text.

    Parameters:
        message (str): Message to respond to.
    """
    # Send defer response (change to "Thinking...")
    await ctx.defer()

    # Generate results
    start_time = time.time()
    result = conversational_generator(message)
    end_time = time.time()

    # Ensure output
    if not result:
        result = "[No Response]"

    # Design embed
    embed = Embed(title="Text Generation Results", color=3743206)
    embed.set_footer(
        text=f"AI Model: {config['CONVERSATION_GENERATION_MODEL']} -- Generation took {end_time-start_time:.2f}s")
    embed.add_field(name="Prompt", value=message, inline=False)
    embed.add_field(name="Result", value=result, inline=False)
    await ctx.respond(embed=embed)

bot.run(config["DISCORD_BOT_TOKEN"])
