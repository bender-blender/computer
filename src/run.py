from builder import Builder
def client_code():
    builder = Builder()
    computer = (builder
                .add_cpu("Intel i9")
                .add_ram("32GB")
                .add_storage("1TB SSD")
                .add_gpu("NVIDIA RTX 3080")
                .build())
    
    print(computer)

# Использование
client_code()