Монтаж pipenv можно установить с Python 3.7 и выше.
https://pypi.org/project/pipenv/

```bash
sudo apt install pipenv
```

Команды:

```bash
  pipenv check
          # Checks for PyUp Safety security vulnerabilities and against PEP 508 markers provided in Pipfile. (Проверяет PyUp Safety на наличие уязвимостей и против Маркеры PEP 508 предоставлены в Pipfile.)
```
```bash
  pipenv clean
          # Uninstalls all packages not specified in Pipfile.lock.(Удаляет все пакеты, не указанные в Pipfile.lock.)
  ```
  ```bash
  pipenv graph
          # Displays currently-installed dependency graph information.(Отображает установленную в данный момент информацию о графе зависимостей.)
  ```
  ```bash
  pipenv install
          # Installs provided packages and adds them to Pipfile, or (if no packages are given), installs all packages from Pipfile.(Устанавливает предоставленные пакеты и добавляет их в Pipfile или (если пакеты не указаны) устанавливает все пакеты из Pipfile.)
  ```
  ```bash
  pipenv lock
          # Generates Pipfile.lock.(Генерирует Pipfile.lock.)
  ```
  ```bash
  pipenv open
            # View a given module in your editor.(Просмотр данного модуля в вашем редакторе.)
  ```
  ```bash
  pipenv requirements
            # Generate a requirements.txt from Pipfile.lock.(Создайте файл requirements.txt из Pipfile.lock.)
  ```
  ```bash
  pipenv run
            # Spawns a command installed into the virtualenv.(Создает команду, установленную в файле virtualenv.)
  ```
  ```bash
  pipenv scripts
            # Lists scripts in current environment config.(Список сценариев в текущей конфигурации среды)
  ```
  ```bash
  pipenv shell
            # Spawns a shell within the virtualenv.(Создает оболочку в файле virtualenv.)
  ```
  ```bash
  pipenv sync
            # Installs all packages specified in Pipfile.lock.(Устанавливает все пакеты, указанные в Pipfile.lock.)
  ```
  ```bash
  pipenv uninstall
            # Uninstalls a provided package and removes it from Pipfile.(Удаляет предоставленный пакет и удаляет его из Pipfile.)
 ```
  ```bash
  pipenv update
            # Runs lock, then sync.(Выполняет блокировку, затем синхронизацию.)
   ```
  ```bash
  pipenv verify
            # Verify the hash in Pipfile.lock is up-to-date.(Убедитесь, что хеш в Pipfile.lock актуален.)
  ```
