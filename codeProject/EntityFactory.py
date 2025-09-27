from codeProject.Background import Background
from codeProject.Const import WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "nivel1-":
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'nivel1-{i}', (0, 0)))
                    list_bg.append(Background(f'nivel1-{i}', (WIDTH, 0)))
                return list_bg

