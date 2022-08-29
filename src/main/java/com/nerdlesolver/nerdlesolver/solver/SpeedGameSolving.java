package com.nerdlesolver.nerdlesolver.solver;

import com.nerdlesolver.nerdlesolver.domain.NerdleGame;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.awt.*;

@Service
public class SpeedGameSolving {

    private Robot speedGameRobot;
    private NerdleGame nerdleGame;

    @Autowired
    public SpeedGameSolving(NerdleGame nerdleGame) {
        this.nerdleGame = nerdleGame;
    }

    public void solving() {
        System.out.println("Solving Nerdle Game");
        nerdleGame.nerdleClassicSolved = true;
    }
}
