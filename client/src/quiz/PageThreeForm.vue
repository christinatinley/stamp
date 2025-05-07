lodgingOptions: [
        { label: 'hotel', value: 'hotel' },
        { label: 'hostel', value: 'hostel' },
        { label: 'airbnb', value: 'airbnb' },
        { label: 'camping', value: 'camping' }
      ]

      <!-- Lodging Preference Select -->
    <div class="flex flex-col">
        <label for="lodging" class="mb-1 text-sm font-medium">
          What type of lodging do you prefer?
        </label>
        <Select
          id="lodging"
          v-model="localForm.lodging"
          :options="lodgingOptions"
          optionLabel="label"
          placeholder="select lodging type"
          class="rounded-md border border-gray-300 outline-none w-full text-black text-sm label-sm p-2"
        />
      </div>