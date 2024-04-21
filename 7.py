import asyncio
import string

async def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

async def count_words(text):
    return len(text.split())

async def reverse_words(text):
    return ' '.join(text.split()[::-1])

async def process_text(text, functions):
    for function in functions:
        text = await function(text)
    return text

async def main():
    text = "Hello, world! Welcome to functional programming."
    functions = [remove_punctuation, reverse_words, count_words]
    result = await process_text(text, functions)
    print(result)

asyncio.run(main())
