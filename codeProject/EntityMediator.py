from codeProject.Const import WIDTH
from codeProject.Enemy import Enemy
from codeProject.EnemyFire import EnemyFire
from codeProject.Entity import Entity
from codeProject.PlayerFire import PlayerFire


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.life = 0
        if isinstance(ent, PlayerFire):
            if ent.rect.left >= WIDTH:
                ent.life = 0
        if isinstance(ent, EnemyFire):
            if ent.rect.right <= 0:
                ent.life = 0
        pass



    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_test = entity_list[i]
            EntityMediator.__verify_collision_window(entity_test)

    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                entity_list.remove(ent)
