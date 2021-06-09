class Covid(pygame.sprite.Sprite):
    def __init__(self, assets):
            
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['covid_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = randint(80, 380)
        self.speed_x = 5
        # self.rect.x = choice([-1500, -1000, -550, 125, 250, 375, 550, 1000, 1500])
        # self.rect.y = choice([800, 1000, 1200, 1400])
        # self.speed_x = 5
        # self.speed_y = 5

    def update(self):
        # if self.rect.x < 0:
            self.rect.x += self.speed_x
            # self.rect.y += 0
            if self.rect.right > abs(self.rect.x):
                self.rect.x = -1000
                self.rect.y = randint(80, 380)
                self.speed_x = 5
                # self.rect.x = choice([-1500, -1000, -550, 125, 250, 375, 550, 1000, 1500])
                # self.rect.y = choice([800, 1000, 1200, 1400])
                # self.speed_x = 5
                # self.speed_y = 5
        # elif self.rect.x > 500:
        #     self.rect.x -= self.speed_x
        #     self.rect.y += 0
        #     if self.rect.left < -self.rect.x:
        #         self.rect.x = choice([-1500, -1000, -550, 125, 250, 375, 550, 1000, 1500])
        #         self.rect.y = choice([800, 1000, 1200, 1400])
        #         self.speed_x = 5
        #         self.speed_y = 5
        # elif 0 < self.rect.x < 500:
        #     self.rect.x += 0
        #     self.rect.y -= self.speed_y
        #     if self.rect.top < -self.rect.y:
        #         self.rect.x = choice([-1500, -1000, -550, 125, 250, 375, 550, 1000, 1500])
        #         self.rect.y = choice([800, 1000, 1200, 1400])
        #         self.speed_x = 5