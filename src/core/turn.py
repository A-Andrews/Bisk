class Turn():

    def __init__(self, factions, board):
        self.factions = factions
        self.board = board
        self.turn_index = 0
        self.reinforcements = 0
        self.start_turn()
        self.selected_region = None
        self.destination_region = None
        self.current_faction = self.factions[self.turn_index]

    def start_turn(self):
        self.current_faction = self.factions[self.turn_index]
        # Calculate reinforcements based on number of territories owned
        self.current_faction.update()
        self.src_sel = None
        self.dst_sel = None

    def end_turn(self):
        self.turn_index = (self.turn_index + 1) % len(self.factions)
        self.start_turn()

    def handle_input(self, pos):
        territory = self.board.get_territory_at_pos(pos)
        if not territory:
            return
        
        if self.src_sel:
            if territory == self.src_sel:
                self.src_sel = None
            elif territory.faction == self.current_faction:
                self.src_sel = territory
                self.dst_sel = None
            else:
                self.dst_sel = territory
                if self.dst_sel.faction != self.current_faction:
                    self.resolve_battle()
                else:
                    self.move_units()


    def resolve_battle(self):
        # Placeholder for battle resolution logic
        print(f"Battle between {self.src_sel} and {self.dst_sel}")
        self.src_sel = None
        self.dst_sel = None

    def move_units(self):
        self.current_faction.move_units(self.src_sel, self.dst_sel)
