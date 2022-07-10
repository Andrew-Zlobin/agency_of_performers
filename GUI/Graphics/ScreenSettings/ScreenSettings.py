from kivy.uix.screenmanager import Screen

class ScreenSettings(Screen):
    def __init__(self, controller, **kwargs):
        super(ScreenSettings, self).__init__(**kwargs)
        self.controller = controller
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
        POPULATION_SIZE = str(self.ids.population_size.text)
        P_CROSSOVER = str(self.ids.p_crossover.text)
        P_MUTATION = str(self.ids.p_mutation.text)
        MAX_GENERATIONS = str(self.ids.max_generations.text)
        individual_creator_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        population_creator_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        cx_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        mut_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        select_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        evaluate_method = list(self.list_of_function_names['individual_creator_method'].keys())[list(self.list_of_function_names['individual_creator_method'].values()).index(self.ids.individual_creator_method.text)]
        new_settings = {'POPULATION_SIZE' : POPULATION_SIZE,
                    'P_CROSSOVER' : P_CROSSOVER,
                    'P_MUTATION' : P_MUTATION,
                    'MAX_GENERATIONS' : MAX_GENERATIONS,
                    'individual_creator_method' : individual_creator_method,
                    'population_creator_method' : population_creator_method,
                    'cx_method' : cx_method,
                    'mut_method' : mut_method,
                    'select_method' : select_method,
                    'evaluate_method' : evaluate_method}
        self.controller.set_new_settings(new_settings)
