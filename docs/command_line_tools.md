
---

### **4️⃣ `docs/command_line_tools.md` - CLI Usage**
```markdown
# 🖥️ Command Line Tools

The **Text Processor Tool** is used via the command line.  
Here are the available commands:

| Option | Description |
|--------|------------|
| `-f, --file` | Path to input text file (required) |
| `-wc, --word-count` | Display total word count |
| `-cc, --char-count` | Display total character count |
| `-lc, --line-count` | Display total line count |
| `-find "word"` | Find occurrences of a word |
| `-r "old" "new"` | Replace a word |

# 🖥️ Command Line Tools

The **Text Processor Tool** allows you to process text files efficiently.  
Use the commands below to interact with your text files.

## 🚀 **Basic Usage**
``` tab="Bash"
python text_processor.py -f sample.txt -wc -cc

python text_processor.py -f sample.txt -r "hello" "hi"

python text_processor.py -f sample.txt -find "hello"


