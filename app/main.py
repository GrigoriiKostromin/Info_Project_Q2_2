#!/usr/bin/env python3
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
#Ich möchte, dass du diesen Kommentar, sobald du die repo gepullt hast ersetzt!

def main() -> None:

    # Bildschirmgröße
    screen_width = 80
    screen_height = 50

    my_files = ['accounts.txt', 'details.csv', 'invite.docx']
   
    # Spieler erscheint in der Mitte
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # Wähle Zeichen aus Tileset
    tileset = tcod.tileset.load_tilesheet(
        "../dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # Bildschirmcreation mit Console
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # Spielschleife
        while True:

            # Spieler wird ausgeben
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            # Vorheriger Schritt wird gelöscht
            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue
                
                # Funktion mit Input wird aufgerufen
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                # Spiel schließen ohne Fehlermeldung
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()