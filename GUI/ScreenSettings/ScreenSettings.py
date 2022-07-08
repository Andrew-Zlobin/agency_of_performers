from kivy.uix.screenmanager import Screen

class ScreenSettings(Screen):
    list_of_function_names = {
            'individual_creator_method' : {'_' : '_',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
            'population_creator_method' : {'_' : '_',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
            'cx_method' : {'cxOnePoint' : 'функция скрещивания',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
            'mut_method' : {'mutation_neighb_trans' : 'трансмутация',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
            'select_method' : {'selTournament' : 'турнир',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
            'evaluate_method' : {'fitness' : 'фитнес',
                                            'another_function' : 'другая функция',
                                            'another_function_2' : 'ещё какая-то функция'},
        }

    def save_settings(self):
        POPULATION_SIZE = self.ids.population_size
        P_CROSSOVER = self.ids.p_crossover
        P_MUTATION = self.ids.p_mutation
        MAX_GENERATIONS = self.ids.max_generations
        individual_creator_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        population_creator_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        cx_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        mut_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        select_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        evaluate_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
