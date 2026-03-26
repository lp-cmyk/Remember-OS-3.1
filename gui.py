receive tkinter as tk
import json

# 读取 CSS 风格配置
with open("style.json", "r", encoding="utf-8") as f:
    style = json.load(f)

root = tk.Tk()
root.title("Remember OS 辅助界面")
root.geometry(style["window_size"])
root.configure(bg=style["bg_color"])

# 标题
label = tk.Label(
    root,
    text="Python 辅助界面",
    bg=style["bg_color"],
    fg=style["text_color"],
    font=style["font"]
)
label.pack(pady=20)

# 按钮
btn = tk.Button(
    root,
    text="启动主程序",
    bg=style["btn_color"],
    fg="white",
    font=style["font"],
    command=lambda: print("run")
)
btn.pack(pady=10)

root.mainloop()
