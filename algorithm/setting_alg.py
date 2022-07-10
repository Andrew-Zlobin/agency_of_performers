class Settings_alg:
  def __init__(self):
    self.const_alg = {           # настройки по умолчанию
    'POPULATION_SIZE' : '5',   # количество индивидуумов в популяции
    'upper_limit_crossover' : '0.9',       # вероятность скрещивания
    'lower_bound_crossover' : '0.2',       # вероятность скрещивания
    'upper_limit_mutation' : '0.9',        # вероятность мутации индивидуума
    'lower_bound_mutation' : '0.2',
    'percentage parents' : '0.5',
    'MAX_GENERATIONS' : '5',    # максимальное количество поколений
    'cx_method' : 'Single Point Mod',
    'mut_method' : 'Transposition adjacent genes',
    'select_method' : 'Better half choice'
    }  


  def set_settings_alg(self, element, key):
    self.const_alg[key] = element


  def get_settings_alg(self, key):
    return self.const_alg[key]


  def set_all_settings_alg(self, config):
    #config = [POPULATION_SIZE, P_CROSSOVER, P_MUTATION, MAX_GENERATIONS, individual_creator_method,
    #population_creator_method, cx_method, mut_method, select_method, evaluate_method]
    i = 0
    for key in self.const_alg:
      self.const_alg[key] = config[i]
      i += 1


  def get_all_settings_alg(self):
    return self.const_alg


  def save_data_config(self, file_name):
    file_name = open(file_name + '.txt', 'w')
    for key in self.const_alg:
      file_name.write(str(self.const_alg[key]) + '\n')
    file_name.close()


  def load_data_config(self, file_name):
    file_name = open(file_name + '.txt', 'r')
    config = []
    for line in file_name:
      config.append(line[: len(line) - 1])
    file_name.close()
    return config


  def set_setting_alg_from_file(self, file_name):
    config = self.load_data_config(file_name)
    self.set_all_settings_alg(config)


###TODO: функция проверки установки параметров