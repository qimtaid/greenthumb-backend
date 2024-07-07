import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5555/events')
      .then(response => setEvents(response.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Event List</h1>
      <Link to="/add">Add Event</Link>
      <ul>
        {events.map(event => (
          <li key={event.id}>
            <Link to={`/edit/${event.id}`}>{event.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EventList;
