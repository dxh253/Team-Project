// EventService.js

import axios from 'axios';

const API_URL = 'http://example.com/api/v1';

class EventService {
  saveEvent(event, accessToken) {
    const url = `${API_URL}/events`;
    const data = {
      name: event.name,
      date: event.date,
      thumbnail: event.thumbnail,
      // additional event properties to be saved
    };
    const headers = {
      Authorization: `Bearer ${accessToken}`,
    };
    return axios.post(url, data, { headers });
  }
}

export default new EventService();
