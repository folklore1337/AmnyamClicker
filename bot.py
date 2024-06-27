import asyncio 

from aiogram import Router, Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Давай Кликать!", web_app=WebAppInfo(
            url="https://0aa6-89-22-2-250.ngrok-free.app"
        )
    )
    return builder.as_markup()

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None: 
    await message.reply(
        "Привет, это Амням Кликер!!!",
        reply_markup=webapp_builder()
    )

async def main() -> None:
    bot = Bot('7037380178:AAG7t1LgPc4fxzIBZOTW4aUHvlYdv7TpTI', ParseMode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
