import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory, useParams } from 'react-router-dom';

function EventForm() {
  const [event, setEvent] = useState({ title: '', description: '', date: '' });
  const history = useHistory();
  const { id } = useParams();

  useEffect(() => {
    if (id) {
      axios.get(`http://localhost:5555/events/${id}`)
        .then(response => setEvent(response.data))
        .catch(error => console.log(error));
    }
  }, [id]);

  const handleChange = e => {
    const { name, value } = e.target;
    setEvent({ ...event, [name]: value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    if (id) {
      axios.put(`http://localhost:5555/events/${id}`, event)
        .then(() => history.push('/'))
        .catch(error => console.log(error));
    } else {
      axios.post('http://localhost:5555/events', event)
        .then(() => history.push('/'))
        .catch(error => console.log(error));
    }
  };

  return (
    <div>
      <h1>{id ? 'Edit Event' : 'Add Event'}</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="title" value={event.title} onChange={handleChange} placeholder="Title" required />
        <textarea name="description" value={event.description} onChange={handleChange} placeholder="Description"></textarea>
        <input type="text" name="date" value={event.date} onChange={handleChange} placeholder="Date" required />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}

export default EventForm;
