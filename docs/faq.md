# ❓ FAQ - Frequently Asked Questions

### 🛠️ **1. How to install dependencies?**
```sh
pip install -r requirements.txt

📂 2. Where should I place sample.txt?
Place it in the same directory as text_processor.py or specify the full path:


python text_processor.py -f /path/to/sample.txt -wc

🏷️ 3. What happens if I use -r "old" "new" without backup?
Your original file will be modified!
To avoid losing data, make a backup first:

s
cp sample.txt sample_backup.txt
python text_processor.py -f sample.txt -r "old" "new"