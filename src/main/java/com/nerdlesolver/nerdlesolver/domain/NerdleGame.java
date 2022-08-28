package com.nerdlesolver.nerdlesolver.domain;

import org.springframework.beans.factory.annotation.Value;

public class NerdleGame {

    @Value("${nerdle.classic.url}")
    public String nerdleClassicUrl;
    public Boolean nerdleClassicSolved = false;

}
