import wx

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class Panel(wx.Panel):
    def __init__(self, parent, path):
        super(Panel, self).__init__(parent, -1)
        bitmap = wx.Bitmap(path)
        bitmap = scale_bitmap(bitmap, 300, 200)
        print bitmap.GetWidth()
        print bitmap.GetHeight()
        control = wx.StaticBitmap(self, -1, bitmap)
        control.SetPosition((10, 10))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = wx.Frame(None, -1, 'Scaled Image')
    panel = Panel(frame, 'D:/CPi/data/text-plain.png')
    frame.Show()
    app.MainLoop()