import express, { Request, Response } from 'express'
import dotenv from 'dotenv'
import { createClient } from '@supabase/supabase-js';

dotenv.config();

const supabase = createClient(
    process.env.SUPABASE_URL!,
    process.env.SUPABASE_KEY!
);

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/health', (req: Request, res: Response) => {
    res.status(200).json({ message: 'OK' });
})

app.get('/players', async (req: Request, res: Response) => {
    const { data, error } = await supabase
        .from('players')
        .select('*');
    if (error) {
        return res.status(500).json({ error: error.message });
    }
    res.status(200).json(data);
})

app.get('/players/:id', async (req: Request, res: Response) => {
    const { id } = req.params;
    const { data, error } = await supabase
        .from('players')
        .select('*')
        .eq('id', id)
        .single();
    if (error) {
        return res.status(404).json({ error: 'Player not found' });
    }
    res.status(200).json(data);
})

app.post('/register', async (req: Request, res: Response) => {
    const { first_name, last_name, email, age, current_team, phone_number } = req.body;
    console.log(req.body);

    const { data, error } = await supabase
        .from('players')
        .insert([
            {
                first_name,
                last_name,
                email,
                age,
                current_team,
                phone_number
            }
        ])
        .select();

    if (error) {
        return res.status(500).json({ error: error.message });
    }

    res.status(201).json(data);

})

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`)
})