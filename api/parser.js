import { parse } from 'json5';

const parser = {
  parseConfig: (configPath) => {
    try {
      const config = parse(require('fs').readFileSync(configPath, 'utf8'));
      return config;
    } catch (error) {
      throw new Error(`Error parsing config file at ${configPath}: ${error.message}`);
    }
  },

  validateConfig: (config) => {
    if (!config.api || !config.api.port || !config.api.host) {
      throw new Error('Invalid config: missing api details');
    }
  },

  getApiHost: (config) => {
    return config.api.host;
  },

  getApiPort: (config) => {
    return config.api.port;
  },
};

export default parser;