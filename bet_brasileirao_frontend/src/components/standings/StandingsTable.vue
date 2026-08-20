<script setup>
import { standingsZone, aproveitamento } from '@/utils/standings'

defineProps({
  rows: { type: Array, required: true }
  /**
   * Cada linha é um Team do backend:
   * { id, name, flag, code, position, playedGames, won, lost, draw, points }
   */
})

const zoneBarClass = {
  libertadores: 'bg-zone-libertadores',
  'pre-lib': 'bg-zone-pre-lib',
  sulamericana: 'bg-zone-sulamericana',
  rebaixamento: 'bg-error'
}

const zonePositionClass = {
  libertadores: 'font-bold text-on-surface',
  'pre-lib': 'text-on-surface-variant',
  sulamericana: 'text-on-surface-variant',
  rebaixamento: 'text-error font-bold'
}
</script>

<template>
  <div class="overflow-x-auto table-scroll w-full">
    <table class="w-full min-w-[640px] text-left border-collapse">
      <thead>
        <tr
          class="text-label-sm font-label-sm text-on-surface-variant uppercase border-b border-surface-container bg-surface-container/50"
        >
          <th class="py-3 px-4 w-12 font-medium">Pos</th>
          <th class="py-3 px-4 font-medium">Clube</th>
          <th class="py-3 px-2 font-bold text-primary w-12 text-center">P</th>
          <th class="py-3 px-2 font-medium w-12 text-center" title="Jogos">J</th>
          <th class="py-3 px-2 font-medium w-12 text-center" title="Vitórias">V</th>
          <th class="py-3 px-2 font-medium w-12 text-center" title="Empates">E</th>
          <th class="py-3 px-2 font-medium w-12 text-center" title="Derrotas">D</th>
          <th class="py-3 px-4 font-medium w-16 text-center" title="Aproveitamento">%</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, index) in rows"
          :key="row.id"
          class="hover:bg-surface-variant/50 transition-colors group"
          :class="index % 2 === 1 ? 'bg-surface-container/10' : ''"
        >
          <td class="py-3 px-4 relative">
            <div
              v-if="standingsZone(row.position)"
              class="absolute left-0 top-0 bottom-0 w-1"
              :class="zoneBarClass[standingsZone(row.position)]"
            ></div>
            <span :class="standingsZone(row.position) ? zonePositionClass[standingsZone(row.position)] : 'text-on-surface-variant'">
              {{ row.position }}
            </span>
          </td>
          <td class="py-3 px-4 flex items-center gap-3">
            <div class="w-6 h-6 rounded-full bg-surface-bright flex items-center justify-center overflow-hidden">
              <img v-if="row.flag" :src="row.flag" alt="" class="w-4 h-4 object-contain" />
            </div>
            <span
              class="group-hover:text-primary transition-colors"
              :class="standingsZone(row.position) === 'rebaixamento' ? 'group-hover:text-error' : ''"
            >
              {{ row.name }}
            </span>
          </td>
          <td class="py-3 px-2 font-odds-display text-odds-display text-on-surface text-center">
            {{ row.points }}
          </td>
          <td class="py-3 px-2 text-on-surface-variant text-center">{{ row.playedGames }}</td>
          <td class="py-3 px-2 text-center text-on-surface-variant">{{ row.won }}</td>
          <td class="py-3 px-2 text-center text-on-surface-variant">{{ row.draw }}</td>
          <td class="py-3 px-2 text-center text-on-surface-variant">{{ row.lost }}</td>
          <td class="py-3 px-4 text-center text-on-surface-variant">{{ aproveitamento(row.points, row.playedGames) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
