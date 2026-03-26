using System;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        // C# 启动 Python 图形界面
        Process.Start("pythonw.exe", "gui.py");
        Console.WriteLine(Python);
        Console.ReadKey();
    }
}
