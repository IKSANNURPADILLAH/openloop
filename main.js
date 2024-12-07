//support multi token with proxy
import fetch from 'node-fetch';
import fs from 'fs';
import chalk from 'chalk';
import { HttpsProxyAgent } from 'https-proxy-agent';
import { banner } from './utils/banner.js';
import { logger } from './utils/logger.js';

const getRandomQuality = () => {
    return Math.floor(Math.random() * (99 - 60 + 1)) + 60;
};

const getProxies = () => {
    return fs.readFileSync('proxy.txt', 'utf8').split('\n').map(line => line.trim()).filter(Boolean);
};

const getTokens = () => {
    return fs.readFileSync('token.txt', 'utf8').split('\n').map(line => line.trim()).filter(Boolean);
};

const makePostRequestWithProxy = async (url, headers, body, proxy) => {
    const proxyAgent = new HttpsProxyAgent(proxy);
    const options = {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(body),
        agent: proxyAgent
    };
    return await fetch(url, options);
};

const shareBandwidth = async (token, proxy, index) => {
    try {
        const quality = getRandomQuality();

        // Log only the index (serial number) of the token being processed
         logger(`Starting bandwidth share for token #${(index + 1)} with proxy: ${chalk.cyan(proxy)}`, 'debug');

        const response = await makePostRequestWithProxy('https://api.openloop.so/bandwidth/share', {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        }, { quality }, proxy);

        if (!response.ok) {
            throw new Error(`Failed to share bandwidth! Status: ${response.statusText}`);
        }

        const data = await response.json();

        const logBandwidthShareResponse = (response) => {
            if (response && response.data && response.data.balances) {
                const balance = response.data.balances.POINT;
                logger(`Token #${chalk.green(index + 1)} - ${chalk.yellow(response.message)} | Score: ${chalk.yellow(quality)} | Total Earnings: ${chalk.yellow(balance)} | Proxy: ${chalk.cyan(proxy)}`, 'info');
            }
        };

        logBandwidthShareResponse(data);
    } catch (error) {
        logger(`Error sharing bandwidth for token #${(index + 1)} with proxy: ${chalk.cyan(proxy)}`, 'error', error.message);
    }
};

const shareBandwidthForAllTokens = async () => {
    let tokens = getTokens();
    let proxies = getProxies();

    // Shuffle proxies to randomize the pairing
    let shuffledProxies = proxies.sort(() => Math.random() - 0.5);

    while (true) {
        // Use Promise.all to run tasks concurrently
        const tasks = tokens.map((token, index) => {
            const proxy = shuffledProxies[index % shuffledProxies.length]; // Reuse proxies if more tokens than proxies
            return shareBandwidth(token, proxy, index);
        });

        try {
            // Wait for all promises to resolve
            await Promise.all(tasks);
            logger('All tokens have been processed. Restarting...');
        } catch (error) {
            logger('Error in sharing bandwidth for some tokens!', 'error', error.message);
        }
    }
};

const main = () => {
    logger(banner, 'debug');
    logger('Starting bandwidth sharing...');
    shareBandwidthForAllTokens(); 
};

main();
