//support multi token with proxy
import fetch from 'node-fetch';
import fs from 'fs';
import chalk from 'chalk';
import { banner } from './utils/banner.js';
import { logger } from './utils/logger.js';

const getRandomQuality = () => {
    return Math.floor(Math.random() * (99 - 60 + 1)) + 60;
};

const getPublicIP = async () => {
    try {
        const response = await fetch('https://api.ipify.org?format=json');
        if (response.ok) {
            const data = await response.json();
            return data.ip;
        } else {
            return "Unable to get IP address";
        }
    } catch (error) {
        console.error('Error fetching public IP:', error);
        return "Unable to get IP address";
    }
};

const getTokens = () => {
    return fs.readFileSync('token.txt', 'utf8').split('\n').map(line => line.trim()).filter(Boolean);
};

const shareBandwidth = async (token, index) => {
    try {
        const quality = getRandomQuality();
        const publicIP = await getPublicIP(); // Await the public IP here

        // Log only the index (serial number) of the token being processed
        logger(`Starting bandwidth share for token #${(index + 1)}`, 'debug');

        const response = await fetch('https://api.openloop.so/bandwidth/share', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ quality }),
        });

        if (!response.ok) {
            throw new Error(`Failed to share bandwidth! Status: ${response.statusText}`);
        }

        const data = await response.json();

        const logBandwidthShareResponse = (response) => {
            if (response && response.data && response.data.balances) {
                const balance = response.data.balances.POINT;
                logger(`Token #${chalk.green(index + 1)} - ${chalk.yellow(response.message)} | Score: ${chalk.yellow(quality)} | Total Earnings: ${chalk.yellow(balance)} | Public IP: ${chalk.yellow(publicIP)}`, 'info');
}
        };

        logBandwidthShareResponse(data);
    } catch (error) {
        logger(`Error sharing bandwidth for token #${(index + 1)}`, 'error', `${chalk.red(error.message)}`);
    }
};

const shareBandwidthForAllTokens = async () => {
    let tokens = getTokens();

    // Use Promise.all to run tasks concurrently with individual error handling
    const tasks = tokens.map((token, index) => {
        return shareBandwidth(token, index).catch(error => {
            logger(`Error with token #${chalk.green(index + 1)}: ${error.message}`, 'error');
        });
    });

    try {
        // Wait for all promises to resolve
        await Promise.all(tasks);
    } catch (error) {
        logger('Error in sharing bandwidth for some tokens!', 'error', error.message);
    }
};

const main = () => {
    logger(banner, 'debug');
    logger('Starting bandwidth sharing each minute...');
    shareBandwidthForAllTokens(); 
    setInterval(shareBandwidthForAllTokens, 60 * 1000); 
};

main();
