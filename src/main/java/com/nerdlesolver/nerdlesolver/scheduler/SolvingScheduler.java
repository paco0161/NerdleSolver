package com.nerdlesolver.nerdlesolver.scheduler;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class SolvingScheduler {

    @Scheduled(cron = "${solving.scheduler.cron}")
    void startSolving() {

    }

}
