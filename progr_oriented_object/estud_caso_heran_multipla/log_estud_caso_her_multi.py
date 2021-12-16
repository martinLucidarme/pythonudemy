class LogMixin:  # Nao precisa das outras classes mais aqui par ser adicionada a outras classes
    @staticmethod  # porque nunca se utiliza o self no método
    def writer(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.writer(f'INFO:{msg}')

    def log_erro(self, msg):
        self.writer(f'ERROR:{msg}')
