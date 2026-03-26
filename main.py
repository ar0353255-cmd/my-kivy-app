from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

class TripleClickApp(App):
    def build(self):
        # إنشاء العداد للتحكم في الضغطات
        self.count = 0
        
        # تصميم الواجهة
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # إضافة نص تعليمي
        self.label = Label(text="welcome to True Squad", font_size='28sp', bold=True)
        self.layout.add_widget(self.label)
        
        # إضافة الزر الرئيسي
        self.btn = Button(
            text=" Click me", 
            size_hint=(1, 0.4),
            background_normal='', # ضروري لتغيير الألوان بوضوح
            background_color=(0.1, 0.5, 0.8, 1) # أزرق هادئ في البداية
        )
        
        # ربط الزر بالوظيفة
        self.btn.bind(on_press=self.handle_clicks)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def handle_clicks(self, instance):
        self.count += 1
        
        if self.count == 1:
            # الضغطة الأولى: تحويل اللون للأصفر
            self.label.text = "1-Ali Al Ridha 2-Hider Adil"
            self.label.color = (1, 1, 0, 1)
            self.btn.text = "Next Click"
            self.btn.background_color = (1, 0.8, 0, 1)
            
        elif self.count == 2:
            # الضغطة الثانية: تحويل اللون للأحمر (تنبيه أو مرحلة ثانية)
            self.label.text = "3-Mahdy Hasan "
            self.label.color = (1, 0.2, 0.2, 1)
            self.btn.text = "next Click"
            self.btn.background_color = (1, 0.3, 0.3, 1)
            
        elif self.count == 3:
            # الضغطة الثالثة: النجاح باللون الأخضر
            self.label.text = "4-Mahdy jabar"
            self.label.color = (0, 1, 0, 1)
            self.btn.text = "next Click"
            self.btn.background_color = (0, 0.8, 0.4, 1)
            
        else:
            # إعادة التصفير بعد الضغطة الثالثة
            self.count = 0
            self.label.text = "The end"
            self.label.color = (1, 1, 1, 1)
            self.btn.text = "back Click"
            self.btn.background_color = (0.1, 0.5, 0.8, 1)

if name == "main":
    TripleClickApp().run()
