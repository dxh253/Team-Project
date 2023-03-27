
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
            <input class="input" type="file" accept="image/*" id="get_image" v-on:change="handleImageUpload">
          </div>
        </div>
        <div class="field">
          <label class="label" for="thumbnail">Thumbnail:</label>
          <div class="control">
            <input class="input" type="file" accept="image/*" id="get_thumbnail" v-on:change="handleThumbnailUpload">
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
          image: null,
          thumbnail: null,
        },
      }
    },
    methods: {
      handleImageUpload(event) {
        if (event.target.files.length > 0) {
          console.log(event.target.files[0])
          this.eventData.get_image = event.target.files[0]
        }
      },
      handleThumbnailUpload(event) {
        if (event.target.files.length > 0) {
          console.log(event.target.files[0])
          this.eventData.get_thumbnail = event.target.files[0]
        }
      },

      submitForm() {
        console.log('submitForm method is executed');
        const formData = new FormData()
        formData.append('id', this.eventData.id)
        formData.append('name', this.eventData.name)
        formData.append('description', this.eventData.description)
        formData.append('venue', this.eventData.venue)
        formData.append('date', this.eventData.date)
        formData.append('get_image', this.eventData.get_image);
        formData.append('get_thumbnail', this.eventData.get_thumbnail);
        getAPI
        .post('latest-events/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
          method: 'POST'
        },
          { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
        .then((response) => {
          console.log('API response data:', response.data);
          // console.log(response.data)
          window.history.back()
        })
        .catch((error) => {
          console.log(error)
          // alert('Something went wrong. Please try again.')
        })

      },
    },
  }
  </script>


  <!-- <template>
    <div class="container">
      <form @submit.prevent="submitForm">
        {% csrf_token %}
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
            <input class="input" type="file" accept="image/*" id="get_image" v-on:change="handleImageUpload">
          </div>
        </div>
        <div class="field">
          <label class="label" for="thumbnail">Thumbnail:</label>
          <div class="control">
            <input class="input" type="file" accept="image/*" id="get_thumbnail" v-on:change="handleThumbnailUpload">
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
        image: null,
        thumbnail: null,
      },
      csrfToken: null,
    }
  },
  mounted() {
    this.getCsrfToken()
  },
  methods: {
    handleImageUpload(event) {
      if (event.target.files.length > 0) {
        console.log(event.target.files[0])
        this.eventData.get_image = event.target.files[0]
      }
    },
    handleThumbnailUpload(event) {
      if (event.target.files.length > 0) {
        console.log(event.target.files[0])
        this.eventData.get_thumbnail = event.target.files[0]
      }
    },
    getCsrfToken() {
      const csrfTokenCookie = document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)')
      if (csrfTokenCookie) {
        this.csrfToken = csrfTokenCookie.pop()
      }
    },
    submitForm() {
      const formData = new FormData()
      formData.append('id', this.eventData.id)
      formData.append('name', this.eventData.name)
      formData.append('description', this.eventData.description)
      formData.append('venue', this.eventData.venue)
      formData.append('date', this.eventData.date)
      formData.append('get_image', this.eventData.get_image)
      formData.append('get_thumbnail', this.eventData.get_thumbnail)

      const headers = {
        'Content-Type': 'multipart/form-data',
        'X-CSRFToken': this.getCsrfToken()
      }

      getAPI.post('latest-events/', formData, { headers })
        .then((response) => {
          console.log(response.data)
          window.history.back()
        })
        .catch((error) => {
          console.log(error)
          alert('Something went wrong. Please try again.')
        })
    },
    methods: {
      getCsrfToken() {
        let csrfToken = null
        const csrfTokenCookie = document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)')
        if (csrfTokenCookie) {
          csrfToken = csrfTokenCookie.pop()
        } else {
          // Generate new CSRF token
          csrfToken = Math.random().toString(36).slice(-12)
          document.cookie = `csrftoken=${csrfToken}; path=/; SameSite=Strict`
        }
        return csrfToken
      }
    },
  }
}



</script> -->