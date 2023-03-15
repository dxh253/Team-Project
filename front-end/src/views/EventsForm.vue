<template>
    <div class="container">
      <form @submit.prevent="submitForm">
        <div class="field">
          <label class="label" for="name">Name:</label>
          <div class="control">
            <input class="input" type="text" id="name" v-model="eventData.name" required>
          </div>
        </div>
        <div class="field">
          <label class="label" for="description">Description:</label>
          <div class="control">
            <textarea class="textarea" id="description" v-model="eventData.description" required></textarea>
          </div>
        </div>
        <div class="field">
          <label class="label" for="venue">Venue:</label>
          <div class="control">
            <textarea class="textarea" id="venue" v-model="eventData.venue" required></textarea>
          </div>
        </div>
        <div class="field">
          <label class="label" for="date">Date:</label>
          <div class="control">
            <input class="input" type="date" id="date" v-model="eventData.date" required>
          </div>
        </div>
        <div class="field">
          <label class="label" for="image">Image:</label>
          <div class="control">
            <input class="input" type="file" accept="image/*" id="image" @change="handleImageUpload" required>
          </div>
        </div>
        <div class="field">
            <label class="label" for="thumbnail">Thumbnail:</label>
            <div class="control">
            <input class="input" type="file" accept="image/*" id="thumbnail" @change="handleThumbnailUpload" required>
            </div>  
        </div>
        <div class="field">
          <div class="control">
            <button class="button is-primary" type="submit">Submit</button>
          </div>
        </div>
      </form>
    </div>
  </template>
  
  
  <script>
  import { getAPI } from '@/plugins/axios'
  
  
  export default {
    data() {
      return {
        eventData: {
          id: '',
          name: '',
          description: '',
          venue: '',
          date: '',
          get_image: null,
          get_thumbnail: null,
        },
      }
    },
    methods: {
      handleImageUpload(event) {
        this.eventData.get_image = event.target.files[0]
      },
      handleThumbnailUpload(event) {
      this.eventData.get_thumbnail = event.target.files[0]
      },
      submitForm() {
        const formData = new FormData();
        formData.append('id', this.eventData.id);
        formData.append('name', this.eventData.name);
        formData.append('description', this.eventData.description);
        formData.append('venue', this.eventData.venue);
        formData.append('date', this.eventData.date);
        formData.append('get_image', this.eventData.get_image);
        formData.append('get_thumbnail', this.eventData.get_thumbnail);
        getAPI.post('api/v1/latest-events/', formData)
        .then(response => {
            console.log(response.data);
            window.history.back();
        })
        .catch(error => {
            console.log(error);
            alert('Something went wrong. Please try again.');
            

        });
      }
    }
  }
  </script>