from rasa.core.actions import Action
from rasa.core.events import SlotSet
from rasa.core.slots import Slot
from rasa.core.domain import Domain
from rasa.core.trackers import DialogueStateTracker
from rasa.core.dispatcher import Dispatcher
from rasa.core.nlg import NaturalLanguageGenerator

# Importer les modules nécessaires

# Définir les réponses possibles
responses = {
    "greet": "Bonjour ! Comment puis-je vous aider ?",
    "goodbye": "Au revoir ! À bientôt.",
    "fallback": "Désolé, je n'ai pas compris. Pouvez-vous reformuler votre demande ?"
}

# Définir les intents
intents = {
    "greet": ["Bonjour", "Salut", "Hello"],
    "goodbye": ["Au revoir", "À plus tard", "Bye"],
    "fallback": ["Je ne sais pas", "Je ne comprends pas"]
}

# Définir les slots
slots = {
    "name": Slot("name", initial_value=None),
    "age": Slot("age", initial_value=None)
}

# Définir les entities
entities = {
    "name": ["John", "Alice", "Bob"],
    "age": ["18", "25", "30"]
}

# Définir les actions
class GreetAction(Action):
    def name(self) -> str:
        return "action_greet"

    def run(self, dispatcher: Dispatcher, tracker: DialogueStateTracker, domain: Domain) -> list:
        dispatcher.utter_message(responses["greet"])
        return []

class GoodbyeAction(Action):
    def name(self) -> str:
        return "action_goodbye"

    def run(self, dispatcher: Dispatcher, tracker: DialogueStateTracker, domain: Domain) -> list:
        dispatcher.utter_message(responses["goodbye"])
        return []

class FallbackAction(Action):
    def name(self) -> str:
        return "action_fallback"

    def run(self, dispatcher: Dispatcher, tracker: DialogueStateTracker, domain: Domain) -> list:
        dispatcher.utter_message(responses["fallback"])
        return []

# Initialiser le chatbot
def initialize_chatbot():
    # Créer le domaine
    domain = Domain(
        intents=intents,
        slots=slots,
        responses=responses,
        entities=entities
    )

    # Créer le tracker
    tracker = DialogueStateTracker("default", slots.values())

    # Créer le dispatcher
    dispatcher = Dispatcher("default", NaturalLanguageGenerator())

    # Exécuter une action de bienvenue
    greet_action = GreetAction()
    greet_action.run(dispatcher, tracker, domain)

# Appeler la fonction d'initialisation du chatbot
initialize_chatbot()