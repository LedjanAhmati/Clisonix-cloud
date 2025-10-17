// deploy.mjs - Neurosonix Cloud Industrial Deployment Script
// Author: Ledjan Ahmati
// License: Closed Source

import { exec } from 'child_process';
import { promisify } from 'util';
const execAsync = promisify(exec);

async function deploy() {
  console.log('🚀 Starting industrial deployment...');

  try {
    // Step 1: Build Docker images
    console.log('🔨 Building Docker images...');
    await execAsync('docker compose build');
    console.log('✅ Docker images built.');

    // Step 2: Restart Docker services
    console.log('🔄 Restarting Docker services...');
    await execAsync('docker compose up -d');
    console.log('✅ Docker services restarted.');

    // Step 3: Health check (optional)
    // You can add health check logic here if needed
    console.log('🩺 Deployment complete.');
  } catch (err) {
    console.error('❌ Deployment failed:', err);
    process.exit(1);
  }
}

deploy();
