from etl.extract import AnimalExtractor
from etl.load import AnimalLoader
from etl.transform import AnimalTransformer


def main():
    extractor = AnimalExtractor()
    transformer = AnimalTransformer()
    loader = AnimalLoader()

    print("Fetching animal IDs...")
    animal_ids = extractor.fetch_animals_ids()
    print(f"Total animals found: {len(animal_ids)}")

    animal_transformed_objects = []
    for animal_id in animal_ids:
        animal = extractor.get_animal_detail(animal_id)
        if animal:
            transformed = transformer.transform(animal)
            animal_transformed_objects.append(transformed)

    print("Uploading animals in batches of 100...")
    loader.load_batches(animal_transformed_objects)
    print("Done!")


if __name__ == "__main__":
    main()
