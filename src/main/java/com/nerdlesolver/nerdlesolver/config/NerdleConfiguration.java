package com.nerdlesolver.nerdlesolver.config;

import com.nerdlesolver.nerdlesolver.domain.NerdleGame;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
@ConditionalOnProperty(name = "scheduling.enabled", matchIfMissing = true)
public class NerdleConfiguration {
    @Bean
    public NerdleGame nerdleGameBean() {
        return new NerdleGame();
    }
}
