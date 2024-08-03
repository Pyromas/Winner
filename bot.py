from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile

bot = Bot(token='YOUR_BOT_TOKEN')
dp = Dispatcher(bot)

DATABASE = 'path_to_your_database.db'
hidden_image_path = 'path_to_hidden_image.png'

@dp.message_handler(commands=['get_my_score'])
async def get_my_score(message: types.Message):
    user_id = message.from_user.id
    m = DatabaseManager(DATABASE)
    info = m.get_winners_img(user_id)
    prizes = [x[0] for x in info]
    
    image_paths = [f'img/{x}' for x in prizes]
    hidden_paths = [hidden_image_path] * len(image_paths)
    
    collage = create_collage(image_paths, hidden_paths)
    
    collage_path = 'collage.png'
    cv2.imwrite(collage_path, collage)
    
    with open(collage_path, 'rb') as photo:
        await bot.send_photo(message.chat.id, InputFile(photo))

if __name__ == '__main__':
    executor.start_polling(dp)
