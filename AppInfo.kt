data class AppInfo(
    val name: String,
    val file: String,
    val icon: String,
    val desc: String,
    val type: String
)

object AppList {
    val allApps = listOf(
        AppInfo(
            name = "计算器",
            file = "calc",
            icon = "🧮",
            desc = "基础四则运算计算器",
            type = "tool"
        ),
        AppInfo(
            name = "记事本",
            file = "note",
            icon = "📒",
            desc = "本地文本笔记，支持持久化保存",
            type = "tool"
        ),
        AppInfo(
            name = "文本工具",
            file = "text",
            icon = "📝",
            desc = "简单输入与弹窗展示",
            type = "tool"
        ),
        AppInfo(
            name = "系统信息",
            file = "info",
            icon = "📜",
            desc = "显示设备与系统状态",
            type = "system"
        ),
        AppInfo(
            name = "系统设置",
            file = "setting",
            icon = "⚙️",
            desc = "背景、窗口、主题设置",
            type = "system"
        ),
        AppInfo(
            name = "简易画板",
            file = "paint",
            icon = "🎨",
            desc = "触摸/鼠标绘图",
            type = "tool"
        ),
        AppInfo(
            name = "全屏时钟",
            file = "clock",
            icon = "🕐",
            desc = "实时时间显示",
            type = "widget"
        ),
        AppInfo(
            name = "桌面便签",
            file = "sticky",
            icon = "📌",
            desc = "快速备忘清单",
            type = "widget"
        )
    )
}