package com.nerdlesolver.nerdlesolver.scheduler;

import com.nerdlesolver.nerdlesolver.domain.NerdleGame;
import com.nerdlesolver.nerdlesolver.solver.SpeedGameSolving;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.awt.*;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

@Service
public class SolvingScheduler {

    private NerdleGame nerdleGame;
    private SpeedGameSolving speedGameSolving;
    
    @Autowired
    public SolvingScheduler(NerdleGame nerdleGame, SpeedGameSolving speedGameSolving) {
        this.nerdleGame = nerdleGame;
        this.speedGameSolving = speedGameSolving;
    }

    @Scheduled(cron = "${solving.scheduler.cron}")
    public void startBrowsing() {
        if (nerdleGame.nerdleClassicSolved) {
            System.out.println("Today's nerdle game is already completed.");
        } else browse(nerdleGame.nerdleClassicUrl);
    }

    private void browse(String url) {
        if (Desktop.isDesktopSupported()) {
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.browse(new URI(url));
            } catch (IOException | URISyntaxException e) {
                e.printStackTrace();
            }
        } else{
            Runtime runtime = Runtime.getRuntime();
            try {
                runtime.exec("rundll32 url.dll,FileProtocolHandler " + url);
                speedGameSolving.solving();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

}
