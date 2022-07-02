import unittest
from Rover import Rover
from Arena import Arena
from Alien import Alien
from Bullet import Bullet
from Props import Props
from Utility import Constants, File, Stats

class MoonPatrolTest(unittest.TestCase):

    def test_cell_control(self):
        constant = Constants.create(Constants, File.readJSON(File, "MOB_lvl1"))  
        arena = Arena((500,500), ("", ""), 0)
        rover1 = Rover(arena, (50,0,0,0,0,0,7), "", 1, constant)
        rover2 = Rover(arena, (0,0,0,0,0,0,5), "", 2, constant)
        alien  = Alien(arena, (0,0,0,0,5,1,0,0), constant)
        prop   = Props(arena, (0,0,0,0,50,50,1,9,0), constant)
        bullet = Bullet(arena, (12,34,0), (0,0,0,0), 10, constant)

        arena.addActor(rover1)
        arena.addActor(rover2)
        arena.addActor(alien)
        arena.addActor(prop)
        arena.addActor(bullet)

        arena.moveAll(12)

        #ASSERT PER I VARI MOVE DEGLI OGGETTI
        self.assertTrue(rover1.position() == (50, 0.6, 35, 30))
        self.assertTrue(rover2.position() == (0, 0.6, 35, 30))
        #self.assertTrue(alien.position() == (0, 0, 0, 0)) #random move
        self.assertTrue(prop.position() == (41, 50, 0, 0))
        self.assertTrue(bullet.position() == (22, 34, 0, 0))
        self.assertTrue(arena.getStats().getScore() == 12)

        #ASSERT SHOOT ROVER
        #MOVE DEL BULLET PUO' CREARE DEI PROPS QUINDI NON SEMPRE E' CORRETTA LA LUNGHEZZA
        self.assertTrue(len(arena.getActors()) == 4)
        rover1.fire()
        self.assertTrue(len(arena.getActors()) == 6)

        #ASSERT COLLIDE
        rover1.collide(rover2)
        self.assertTrue(not rover1.isDead())
        self.assertTrue(not rover2.isDead())

        rover1.collide(Bullet(arena, (12,34,2), (0,0,0,0), 10, constant))
        self.assertTrue(rover1.isDead())

        rover1.collide(Props(arena, (0,0,0,0,50,50,0,9,0), constant))
        self.assertTrue(rover1.isDead())

        alien.collide(Alien(arena, (0,0,0,0,5,0,0,0), constant))
        self.assertTrue(alien in arena.getActors())

        alien.collide(Bullet(arena, (12,34,1), (0,0,0,0), 10, constant))
        self.assertTrue(alien not in arena.getActors())

        bullet.collide(Props(arena, (0,0,0,0,50,50,0,9,0), constant))
        self.assertTrue(bullet not in arena.getActors())

        bullet.collide(Rover(arena, (50,0,0,0,0,0,7), "", 1, constant))
        self.assertTrue(bullet not in arena.getActors())

        prop.collide(Rover(arena, (0,0,0,0,0,0,5), "", 2, constant))
        self.assertTrue(prop in arena.getActors())

        prop.collide(Bullet(arena, (12,34,2), (0,0,0,0), 10, constant))
        self.assertTrue(prop in arena.getActors())

        prop.collide(Bullet(arena, (12,34,0), (0,0,0,0), 10, constant))
        self.assertTrue(prop not in arena.getActors())

        
        #DOPO AVER AGGIUNTO E TOLTO GLI OGGETTI PER I VARI COLLIDE VERIFICO LA LUNGHEZZA
        self.assertTrue(len(arena.getActors()) == 13)

        

if __name__ == '__main__':
        unittest.main()