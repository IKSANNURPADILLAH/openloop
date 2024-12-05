import fs from 'fs';
import fetch from 'node-fetch';

// Function to read tokens from a file
const readTokens = () => {
  const tokens = fs.readFileSync('token.txt', 'utf8').trim().split('\n');
  return tokens;
};

// Function to complete a mission using a specific token
const completeMission = async (missionId, token) => {
  try {
    const response = await fetch(`https://api.openloop.so/missions/${missionId}/complete`, {
      headers: {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        "authorization": `Bearer ${token}`,
        "priority": "u=1, i",
        "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
      },
      referrerPolicy: "strict-origin-when-cross-origin",
      body: null,
      method: "GET"
    });

    const data = await response.json();
    console.log(`Mission ${missionId} completed with token: ${token}, Data:`, data);
  } catch (error) {
    console.error(`Error completing mission ${missionId} with token ${token}:`, error);
  }
};

// Function to execute missions sequentially with each token
const executeMissionsWithTokens = async (missionIds, tokens) => {
  for (let tokenIndex = 0; tokenIndex < tokens.length; tokenIndex++) {
    const token = tokens[tokenIndex];

    // Loop through each mission ID and complete the mission with the current token
    for (const missionId of missionIds) {
      await completeMission(missionId, token);
    }
  }
};

// List of mission IDs
const missionIds = [16, 15, 14, 13, 12, 11, 10, 9];

// Read tokens from the file
const tokens = readTokens();

// Execute missions with the available tokens
executeMissionsWithTokens(missionIds, tokens);