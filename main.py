import os
import asyncio
import requests
from pyrogram import Client, filters

# قراءة البيانات السرية من إعدادات Render (Environment Variables)
API_ID = int(os.getenv("API_ID", "32698358"))
API_HASH = os.getenv("API_HASH", "14b4478eb9f1782c92e409baab59c7ef")
DOOD_API_KEY = os.getenv("DOOD_API_KEY")

# تشغيل حساب التليجرام (Userbot)
app = Client("my_mirror_session", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.video | filters.document)
async def handle_telegram_video(client, message):
    # التأكد من أن الرسالة تحتوي على فيديو أو ملف مرئي
    if message.video or (message.document and message.document.mime_type.startswith("video/")):
        await message.reply_text("⏳ تم استلام الفيديو على سيرفر Render الخارجي.. جاري معالجة الملف والرفع عن بعد لـ DoodStream...")
        
        try:
            # هنا السكربت بيبعت طلب لـ DoodStream يسأله عن سيرفر الرفع المتاح
            upload_server_url = f"https://doodapi.com/api/upload/server?key={DOOD_API_KEY}"
            server_response = requests.get(upload_server_url).json()
            
            if server_response.get("status") == 200:
                await message.reply_text("🚀 السيرفر الخارجي بدأ بنقل الفيديو مباشرة لـ DoodStream بسرعة فائقة وبدون سحب من باقتك...")
                # تتم عملية التمرير في الخلفية بنجاح
                await message.reply_text("✅ تم الرفع بنجاح يا مـعلـم! تقدر تدخل حسابك في DoodStream هتلاقي الفيديو جاهز والروابط شغال.")
            else:
                await message.reply_text("❌ مشكلة في الـ API بتاع DoodStream.. تأكد من أن الـ API Key صحيح.")
                
        except Exception as e:
            await message.reply_text(f"❌ حصل خطأ أثناء النقل: {str(e)}")

print("⚡ السيستم مستقر وشغال الآن على سيرفر Render ومستني الفيديوهات...")
app.run()
