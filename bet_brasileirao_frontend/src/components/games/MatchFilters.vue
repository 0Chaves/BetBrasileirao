<script setup>
defineProps({
  active: { type: String, required: true }
})
defineEmits(['update:active'])

const filters = [
  { key: 'live', label: 'Ao Vivo' },
  { key: 'upcoming', label: 'Próximos' },
  { key: 'finished', label: 'Encerrados' }
]
</script>

<template>
  <div class="flex gap-md mb-lg overflow-x-auto hide-scrollbar">
    <button
      v-for="filter in filters"
      :key="filter.key"
      type="button"
      class="px-lg py-sm rounded-full font-label-sm text-label-sm whitespace-nowrap transition-colors"
      :class="
        active === filter.key
          ? 'bg-primary-container text-on-primary-container shadow-sm hover:opacity-90'
          : 'bg-surface-variant text-on-surface-variant hover:bg-surface-container-high'
      "
      @click="$emit('update:active', filter.key)"
    >
      {{ filter.label }}
    </button>
  </div>
</template>
