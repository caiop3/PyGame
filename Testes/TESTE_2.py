def final_screen(screen):

    clock = pygame.time.Clock()

    final_screen = pygame.image.load(os.path.join(IMG_DIR, 'sky_fim.png')).convert()
    final_screen = pygame.transform.scale(final_screen, (WIDTH, HEIGHT))

    end = True
    while end:

        clock.tick(FPS)

        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                end = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    state = START
                    end = False
        
        screen.blit(final_screen, (0,0))

        pygame.display.flip()
    
    return state