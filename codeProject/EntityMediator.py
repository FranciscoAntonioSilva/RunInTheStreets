from codeProject.Const import WIDTH
from codeProject.Enemy import Enemy
from codeProject.EnemyFire import EnemyFire
from codeProject.Entity import Entity
from codeProject.Player import Player
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
    def __verify_collision_entity(ent1, ent2):
        valid_collision = False
        #Talvez precise mudar a partir do segundo if para elif
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerFire):
            valid_collision = True
        if isinstance(ent1, PlayerFire) and isinstance(ent2, Enemy):
            valid_collision = True
        if isinstance(ent1, Player) and isinstance(ent2, EnemyFire):
            valid_collision = True
        if isinstance(ent1, EnemyFire) and isinstance(ent2, Player):
            valid_collision = True
    #Validação das colisões
        if valid_collision:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):
                ent1.life -= ent2.dano #No exemplo do professor vai estar como damage
                ent2.life -= ent1.dano
                ent1.last_dano = ent2.name
                ent2.last_dano = ent1.name


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def mark_score(enemy: Enemy, entity_list: list[Entity]): #No exemplo do professor estar como give_score
        if enemy.last_dano == 'PlayerShot':
            for ent in entity_list:
                if ent.name == 'Player':
                    ent.pontuacao += enemy.pontuacao



    @staticmethod
    def verify_life(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.life <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.mark_score(ent, entity_list)
                entity_list.remove(ent)
