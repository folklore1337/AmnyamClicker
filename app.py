import flet as ft
import asyncio
import pygame
pygame.init()

sound = pygame.mixer.Sound("mili.wav")

async def main(page: ft.Page) -> None:
    page.title = "Amnyam Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="Fulbo Argenta")


    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)
    

        image.scale = 0.95

        image.animate_scale = ft.Animation(
            duration=300,  
            curve=ft.AnimationCurve.BOUNCE_OUT,  
        )
        image.scale = 1.1  
        await page.update_async()

        await asyncio.sleep(0.3)  
        image.scale = 1.0  
        await page.update_async()
        progress_bar.value += (1 / 50)

        if score.data % 50 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="🍬 +50",
                    size=20,
                    color="#22c764",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#0f6"
            )
            page.snack_bar.open = True
            progress_bar.value = 0

        if score.data % 50 == 0:
            image_path = "амням.png"
            image.src = image_path  
        if score.data % 100 == 0:
            image_path = "AMNJAMUS_021.png"
            image.src = image_path  
        if score.data % 150 == 0:
            image_path = "kekus.png"
            image.src = image_path 
            
        if score.data == 50:
            sound.play()
        elif score.data == 100:
            sound.play()
        elif score.data == 150:
            sound.play()
        elif score.data == 200:
            sound.play()


        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()



    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="amnyam.png",
        fit=ft.ImageFit.CONTAIN, 
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value= 0,
        width=page.width - 100,
        bar_height=20,
        color="#00ff37",
        bgcolor="#557f5f"
    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        ),
    )
    await page.update_async()



if __name__ == "__main__":
    ft.app(target=main, view=None, port=8000)