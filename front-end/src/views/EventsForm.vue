<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="field">
        <label class="label" for="name">Name:</label>
        <div class="control">
          <input class="input" type="text" id="name" v-model="eventData.name" required />
        </div>
      </div>
      <div class="field">
        <label class="label" for="category">Category:</label>
        <div style="display: flex; justify-content: space-around">
          <div>
            <label style="display: inline" for="study-group">Event </label>
            <input type="radio" id="event" name="event" value="1" v-model="eventData.category" />
          </div>
          <div>
            <label style="display: inline" for="study-group">Study group
            </label>
            <input type="radio" id="study-group" name="study-group" value="2" v-model="eventData.category" />
          </div>
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
          <input class="input" type="date" id="date" v-model="eventData.date" required />
        </div>
      </div>
      <div class="field">
        <label class="label" for="image">Image:</label>
        <div class="control">
          <input class="input" type="file" accept="image/*" id="get_image" v-on:change="handleImageUpload" />
        </div>
      </div>
      <div class="field">
        <label class="label" for="thumbnail">Thumbnail:</label>
        <div class="control">
          <input class="input" type="file" accept="image/*" id="get_thumbnail" v-on:change="handleThumbnailUpload" />
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
import { getAPI } from "@/plugins/axios";
import jwt_decode from "jwt-decode";

export default {
  data() {
    return {
      eventData: {
        id: "",
        name: "",
        category: "",
        description: "",
        venue: "",
        date: "",
        image: null,
        thumbnail: null,
      },
    };
  },
  methods: {
    handleImageUpload(event) {
      if (event.target.files.length > 0) {
        console.log(event.target.files[0]);
        this.eventData.get_image = event.target.files[0];
      }
    },
    handleThumbnailUpload(event) {
      if (event.target.files.length > 0) {
        console.log(event.target.files[0]);
        this.eventData.get_thumbnail = event.target.files[0];
      }
    },

    submitForm() {
      console.log("submitForm method is executed");
      const token = localStorage.getItem("access");
      const decodedToken = jwt_decode(token);
      const ownerId = decodedToken.user_id;

      const formData = new FormData();
      formData.append("id", this.eventData.id);
      formData.append("name", this.eventData.name);
      formData.append("category", this.eventData.category);
      formData.append("description", this.eventData.description);
      formData.append("venue", this.eventData.venue);
      formData.append("date", this.eventData.date);
      formData.append("get_image", this.eventData.get_image);
      formData.append("get_thumbnail", this.eventData.get_thumbnail);
      formData.append("owner", parseInt(ownerId));
      getAPI
        .post("api/v1/latest-events/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
          method: "POST",
        })
        .then((response) => {
          console.log("API response data:", response.data);
          // console.log(response.data)
          window.history.back();
        })
        .catch((error) => {
          console.log(error.response.data);
          // alert('Something went wrong. Please try again.')
        });
    },
  },
};
</script>