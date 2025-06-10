import { render, screen } from '@testing-library/react'
import Home from '../index'

describe('Home', () => {
  it('renders a heading', () => {
    render(<Home />)
    
    const heading = screen.getByRole('heading', {
      name: /habit tracker/i,
    })

    expect(heading).toBeInTheDocument()
  })

  it('renders welcome message', () => {
    render(<Home />)
    
    const message = screen.getByText(/welcome to your habit tracking journey/i)
    expect(message).toBeInTheDocument()
  })
}) 