# winclip

利用 Windows 系统的剪贴板，封装了一个方便的 ClipBoard 类，提供了

- read 读取剪贴板中内容，可指定特定的格式，或者自动推导
- write 将内容写入到剪贴板中
- listen 监听剪贴板的变化，指定传入的回调函数（不处理异常）

等功能。

在 demo 包中，提供了以下服务：

1. demo.print_clipboard_on_change 当剪贴板更新时，将剪贴板的内容打印在控制台中
2. demo.texclip 当剪贴板更新时，将内容用 latex 编译，用 imagemagick 转换为 png 保存在当前工作目录中。
