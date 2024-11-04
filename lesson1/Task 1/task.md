

This project visualizes the distribution of video games across four platforms (PS4, XOne, PC, WiiU) by genre. Using matplotlib, it guides users through loading, filtering, and plotting data to create a clear, customized grouped bar chart.
![](example.png)




## Task 1: Add the Dataset to the Repository

When working on a data visualization project, keeping the dataset organized and accessible is crucial. Here are a few common ways to manage datasets in projects: **For this lesson, we will assume that the dataset is in the project directory.**





1. ####  **Including the Dataset in the Repository:**

    This approach involves adding the dataset directly to the project’s repository. It’s ideal for smaller datasets that need to be accessed frequently by all collaborators. This ensures that all project files are kept together, simplifying version control.
        
        data = pd.read_csv('dataset.csv')


2. ####  **Referencing an External Path:**
    If you have a large dataset located outside your project directory, you can reference it by its full file path, keeping the project lightweight and reducing duplication.
                    
         data = pd.read_csv('/path/to/your/dataset.csv')



3. #### **Using Cloud Storage Links:**
    For very large datasets that are impractical to store locally, cloud storage (e.g., Google Drive or AWS S3) can be used to host the dataset, allowing access without keeping it in the project directory. This is ideal for sharing data with multiple collaborators or managing large files. 

        url = 'https://drive.google.com/uc?id=YOUR_FILE_ID&export=download'
        
        data = pd.read_csv(url)

Now we have an error which we will fix in the next step.