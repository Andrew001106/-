from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Темная тема "Хакера"
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class AdminPanel(App):
    def build(self):
        # Главный контейнер
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 1. Заголовок
        header = Label(
            text="[ COMMAND CENTER ]", 
            font_size='24sp', 
            color=(0, 1, 0, 1), # Зеленый текст
            size_hint_y=0.1,
            bold=True
        )
        main_layout.add_widget(header)

        # 2. Список подключенных устройств (Прокручиваемый)
        main_layout.add_widget(Label(text="Подключенные устройства:", size_hint_y=0.05))
        
        scroll = ScrollView(size_hint=(1, 0.3))
        self.victim_list = BoxLayout(orientation='vertical', size_hint_y=None)
        self.victim_list.bind(minimum_height=self.victim_list.setter('height'))
        
        # Пример устройства в списке
        btn = Button(text="ID: 99281 (Xiaomi Mi 11) - ONLINE", size_hint_y=None, height=40, background_color=(0, 0.5, 0, 1))
        self.victim_list.add_widget(btn)
        
        scroll.add_widget(self.victim_list)
        main_layout.add_widget(scroll)

        # 3. Поле для ввода сообщения жертве
        main_layout.add_widget(Label(text="Текст для отправки на экран:", size_hint_y=0.05))
        self.msg_input = TextInput(
            text="Твой телефон взломан!", 
            multiline=False, 
            size_hint_y=0.1,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        main_layout.add_widget(self.msg_input)

        # 4. Кнопки управления
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=5)
        
        btn_send = Button(text="ОТПРАВИТЬ\nТЕКСТ", on_press=self.send_text)
        btn_screen = Button(text="СМОТРЕТЬ\nЭКРАН", on_press=self.view_screen)
        btn_files = Button(text="ФАЙЛЫ\nЖЕРТВЫ", on_press=self.get_files)
        
        buttons_layout.add_widget(btn_send)
        buttons_layout.add_widget(btn_screen)
        buttons_layout.add_widget(btn_files)
        
        main_layout.add_widget(buttons_layout)

        # 5. Кнопка самоуничтожения ловушки
        btn_kill = Button(
            text="УДАЛИТЬ ЛОВУШКУ С УСТРОЙСТВА", 
            size_hint_y=0.1, 
            background_color=(0.7, 0, 0, 1)
        )
        main_layout.add_widget(btn_kill)

        return main_layout

    def send_text(self, instance):
        print(f"Отправка текста: {self.msg_input.text}")

    def view_screen(self, instance):
        print("Запрос трансляции экрана...")

    def get_files(self, instance):
        print("Доступ к папкам открыт...")

if __name__ == '__main__':
    AdminPanel().run()
    